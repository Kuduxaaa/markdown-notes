<template>
    <div class="page">
        <div class="title">
            <h1 class="title-text" v-if="!render">{{ internalTitle }}</h1>
            <input v-else type="text" v-model="internalTitle" placeholder="Untitled">
        </div>

        <div class="content">
            <Markdown v-if="!render" :source="internalContent" class="markdown-body" :html="true" />
            <textarea v-else name="page-content" ref="contentTextarea" placeholder="Enter content here..."
                v-model="internalContent"></textarea>
        </div>
    </div>
</template>

<script>
import Markdown from 'vue3-markdown-it';

export default {
    components: {
        Markdown
    },

    props: {
        render: {
            type: Boolean,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        content: {
            type: String,
            required: true
        }
    },

    data() {
        return {
            internalTitle: this.title,
            internalContent: this.content
        };
    },

    watch: {
        render(editMode) {
            if (!editMode) {
                this.$emit('update-post', { title: this.internalTitle, content: this.internalContent });
            }
        },

        internalTitle: {
            handler: function (newInternalTitle, oldInternalTitle) {
                this.$emit('update-title', newInternalTitle);
            },

            deep: true
        },

        internalContent: {
            handler: function (newInternalContent, oldInternalContent) {
                this.$emit('update-content', newInternalContent);
            },

            deep: true
        }
    }
}
</script>


<style scoped>
.page {
    display: block;
}

.content {
    width: 100%;
    text-align: left;
    margin-top: 30px;
    font-size: 18px;
    height: 100vh;
}

.content textarea {
    width: 100%;
    height: 100%;
    border: none;
    outline: none;
    resize: none;
    font-size: 18px;
    background-color: transparent;
    color: #ddd;
    font-family: 'Courier New', Courier, monospace;
}

.title input {
    width: 100%;
    font-size: 40px;
    background-color: transparent;
    border: none;
    outline: none;
    color: #fff;
    font-weight: 600
}

.title-text {
    font-size: 40px;
    color: #fff;
    font-weight: 600;
}

p,
pre,
h1,
h2,
h3,
h4 {
    margin: 12px auto;
}
</style>
