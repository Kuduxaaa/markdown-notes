<template>
    <div>
        <SidebarComponent ref="sidebar" @width-updated="updateContentMargin" @edit-mode-changed="togglePreviw" />

        <IndicatorComponent :data="indicatorData" />

        <div class="content" ref="content">
            <div v-if="currentPost !== null" class="container">
                <ContentComponent :key="currentPost.id" :render="editMode" :title="currentPost.title"
                    :content="currentPost.content" @update-indicator="updateIndicator"
                    @update-content="calculateIndicators" @update-post="updatePost" />
            </div>
            <div v-else class="container">
                <h1>There is no posts to see!</h1>
                <p class="text-muted mt-2">Add new post or select from left sidebar ️‍🔥</p>
            </div>
        </div>
    </div>
</template>
<script>
import SidebarComponent from '@/components/SiderbarComponent.vue';
import IndicatorComponent from '@/components/IndicatorComponent.vue';
import ContentComponent from '@/components/ContentComponent.vue';

export default {
    name: 'App',
    components: {
        SidebarComponent,
        IndicatorComponent,
        ContentComponent
    },

    data() {
        return {
            editMode: false,
            indicatorData: {
                characters: 0,
                words: 0
            },

            currentPost: null,
        }
    },

    beforeMount() {
        this.reloadPost();
    },

    watch: {
        '$route.params.id': {
            immediate: true,

            handler() {
                this.reloadPost();
            }
        }
    },

    methods: {
        updateContentMargin() {
            const sidebarWidth = this.$refs.sidebar.sidebarWidth;
            this.$refs.content.style.width = `calc(100% - ${sidebarWidth}px)`;
            this.$refs.content.style.marginLeft = `${sidebarWidth}px`;
        },

        updateIndicator(content) {
            this.contentData = content;
            this.calculateIndicators(content);
        },

        calculateIndicators(content) {
            const characterCount = content.length;
            const wordCount = content.trim().split(/\s+/).filter(Boolean).length;

            this.indicatorData = {
                characters: characterCount,
                words: wordCount
            };
        },

        async reloadPost() {
            try {
                const postId = this.$route.params.id;
                const currentPost = await this.$posts.get(postId);

                if (currentPost.success) {
                    this.currentPost = currentPost.data;

                    if (this.currentPost !== null && this.currentPost.content.length > 0) {
                        this.calculateIndicators(this.currentPost.content);
                    } else {
                        this.calculateIndicators('');
                    }
                }

            } catch (error) {
                console.error('Error reloading post:', error);
            }
        },


        togglePreviw(editMode) {
            this.editMode = editMode;
        },

        updatePost(data) {
            const postId = this.currentPost.id;
            const response = this.$posts.update(postId, data.title, data.content);

            if (this.currentPost.title !== data.title) {
                response.then(() => {
                    this.emitter.emit('reload-sidebar');
                })
            }
        }
    }
}
</script>


<style scoped>
.content {
    margin-left: 340px;
    width: calc(100% - 340px);
    transition: margin-left 0.3s ease;
    display: flex;
    justify-content: center;
    padding-top: 70px;
}

.container {
    width: 50%;
    padding: 40px 30px;
}

@media only screen and (max-width: 1180px) {
    .content {
        margin-left: 0px !important;
        width: 100% !important;
    }

    .container {
        width: calc(100% - 48px);
        padding: 60px 24px;
    }
}
</style>
