<template>
    <div :class="{ 'sidebar closed': !isSidebarOpened, 'sidebar': isSidebarOpened }"
        :style="{ width: sidebarWidth + 'px' }" ref="sidebar">
        <div class="resize-handle" @mousedown="startResize" title="Resize"></div>

        <SearchComponent :isSearchOpened="isSearchOpened" @search="doSearch" />

        <div class="sidebar-tools">
            <div class="tool" @click="createNewPost">
                <div class="tool-icon">
                    <BootstrapIcon icon="plus-circle" size="lg" />
                </div>
            </div>

            <div class="tool search" @click="search">
                <div class="tool-icon">
                    <BootstrapIcon icon="search" size="lg" />
                </div>
            </div>

            <div class="tool" @click="deletePost">
                <div class="tool-icon">
                    <BootstrapIcon icon="trash" size="lg" />
                </div>
            </div>

            <div :class="{ 'tool active': editMode, 'tool': !editMode }" @click="preview">
                <div class="tool-icon">
                    <BootstrapIcon :icon="(!editMode) ? 'pencil' : 'floppy'" size="lg" />
                </div>
            </div>

            <div class="tool menu-open" @click="toggleSidebar">
                <div class="tool-icon">
                    <BootstrapIcon :icon="(!isSidebarOpened) ? 'list' : 'x'" size="lg" />
                </div>
            </div>
        </div>

        <div class="items" v-if="this.posts.length > 0">
            <div class="post" v-if="!isSearching">
                <SidebarItemComponent v-for="post in this.posts" v-bind:key="post.title" :name="post.title"
                    :id="post.id" />
            </div>
            <div class="results" v-else>
                <SidebarItemComponent v-for="post in this.searchResults" v-bind:key="post.title" :name="post.title"
                    :id="post.id" />
            </div>
        </div>

        <div class="items" v-else>
            <div class="text-center">
                <p class="text-muted mt-2">Alas, the land of emptiness!</p>
                <p class="text-muted mt-2">Behold, the void yearns for your words!</p>
                <p class="text-muted mt-2">With a mere tap,</p>
                <p class="text-muted mt-2">Summon the legendary plus icon
                    <BootstrapIcon icon="plus-circle" size="sm" /> and craft digital wonders!
                </p>
            </div>

        </div>

    </div>
</template>

<script>
import SidebarItemComponent from '@/components/SidebarItemComponent.vue';
import SearchComponent from '@/components/SearchComponent.vue';
// import eventBus from '../eventBus'

export default {
    name: 'SidebarComponent',
    data() {
        return {
            isResizing: false,
            startX: 0,
            startWidth: 0,
            sidebarWidth: 340,
            editMode: false,
            isSidebarOpened: false,
            isSearchOpened: false,
            posts: [],
            searchResults: [],
            isSearching: false,
        };
    },

    components: {
        SidebarItemComponent,
        SearchComponent,
    },

    mounted() {
        if (window.innerWidth >= 1180) {
            this.isSidebarOpened = true;
        }

        this.updateSidebarWidth();
        this.$emit('edit-mode-changed', this.editMode);
        this.reloadData();

        window.addEventListener('click', this.outSideClick);
        this.emitter.on('reload-sidebar', this.reloadData);
    },

    beforeUnmount() {
        window.removeEventListener('click', this.outSideClick);
    },

    methods: {
        outSideClick(event) {
            if (!event.target.closest('.tool.search')) {
                this.isSearchOpened = false;
                this.isSearching = false;
            }
        },

        search() {
            this.isSearchOpened = true;

            if (window.innerWidth <= 1180) {
                this.toggleSidebar();
            }
        },

        startResize(event) {
            this.isResizing = true;
            this.startX = event.clientX;
            this.startWidth = this.$refs.sidebar.clientWidth;

            document.addEventListener('mousemove', this.resize);
            document.addEventListener('mouseup', this.stopResize);
        },

        async reloadData() {
            try {
                const posts = await this.$posts.getAll();

                if (posts.success) {
                    this.posts = posts.data;
                }

            } catch (error) {
                console.error('Error reloading data:', error);
            }
        },


        resize(event) {
            if (this.isResizing) {
                let width = this.startWidth + (event.clientX - this.startX);
                width = Math.min(width, 1500);

                this.sidebarWidth = Math.max(250, width);
            }
        },

        async createNewPost() {
            try {
                const newPost = await this.$posts.create('Untitled', '');

                if (newPost.success) {
                    this.$router.push({ name: 'Post', params: { id: newPost.data.id } });
                    this.$emit('edit-mode-changed', true);
                    this.editMode = true;

                    await this.reloadData();
                }
            } catch (error) {
                console.error('Error creating new post:', error);
            }
        },


        doSearch(query) {
            if (query.length > 0) {
                this.isSearching = true;
                this.searchResults = this.posts.filter(post => post.title.toLowerCase().includes(query.toLowerCase()));
            } else {
                this.isSearching = false;
            }
        },


        stopResize() {
            this.isResizing = false;
            document.removeEventListener('mousemove', this.resize);
            document.removeEventListener('mouseup', this.stopResize);
        },

        preview() {
            this.editMode = !this.editMode;
            this.$emit('edit-mode-changed', this.editMode);
        },

        toggleSidebar() {
            this.isSidebarOpened = !this.isSidebarOpened;
        },

        updateSidebarWidth() {
            this.sidebarWidth = this.$refs.sidebar.clientWidth;
        },

        async deletePost() {
            try {
                const postId = this.$route.params.id;
                await this.$posts.deletePost(postId);
                await this.reloadData();

                const redirectId = this.posts.length > 0 ? this.posts[0].id : 0;
                this.$router.push({ name: 'Post', params: { id: redirectId } });

            } catch (error) {
                console.error('Error deleting post:', error);
            }
        }

    },

    watch: {
        sidebarWidth(newWidth, oldWidth) {
            if (newWidth !== oldWidth) {
                this.$emit('width-updated', newWidth);
            }
        },

        '$route.params.id': {
            immediate: true,

            handler() {
                if (window.innerWidth <= 1180) {
                    this.isSidebarOpened = false;
                }
            }
        }
    }
}
</script>

<style scoped>
.sidebar {
    width: 340px;
    height: 100%;
    background-color: var(--background-default);
    border-right: 1px solid #363636;
    position: fixed;
    top: 0;
    left: 0;
    overflow: hidden;
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    transition: .3s left;
}

.sidebar-tools {
    display: flex;
    width: 100%;
    justify-content: center;
    padding: 10px 0px;
}

.sidebar-tools .tool {
    margin: 5px 0px;
    cursor: pointer;
    text-align: center;
    padding: 7px;
    border-radius: 6px;
    transition: .2s all;
}

.sidebar-tools .tool .tool-icon {
    color: #9f9f9f;
}

.sidebar-tools .tool:hover,
.sidebar-tools .tool.active {
    background-color: #363636;
}

.resize-handle {
    width: 3px;
    height: 100%;
    background-color: transparent;
    position: absolute;
    right: 0;
    top: 0;
    cursor: ew-resize;
    transition: .3s all;
    z-index: 999999999999;
}

.resize-handle:hover {
    background-color: #8068fb;
    box-shadow: 0px 0px 8px #8168fb;
}

.sidebar.closed {
    left: -100% !important;
}

.menu-open {
    display: none;
}

.items {
    padding: 14px;
    height: calc(100% - 100px);
    overflow: auto;
}

@media only screen and (max-width: 1180px) {
    .sidebar {
        position: fixed;
        width: 100% !important;
        z-index: 9999;
        padding-top: 70px;
        top: 0;
        left: 0;
    }

    .sidebar-tools {
        padding: 3px auto;
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        background-color: #262626a8;
        backdrop-filter: blur(5px);
        border-bottom: 1px solid #363636;
        box-shadow: 0px 0px 10px #363636;
    }

    .menu-open {
        display: block;
    }
}
</style>
