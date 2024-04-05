<template>
    <div @click.stop :class="{ 'search': !isSearchOpened, 'search open': isSearchOpened }">
        <input type="search" v-model="query" @click.stop placeholder="Search..." autofocus=""
            v-on:keyup="handleSearch" />
    </div>
</template>

<script>
export default {
    name: 'SearchComponent',

    data() {
        return {
            query: '',
        }
    },

    props: {
        isSearchOpened: {
            required: false,
            type: Boolean,
            default: false,
        }
    },

    methods: {
        handleSearch() {
            this.$emit('search', this.query)
        }
    }
}
</script>

<style scoped>
.search {
    width: 100%;
    position: absolute;
    background-color: var(--background-default);
    border-bottom: 1px solid #363636;
    left: 0;
    top: -68px;
    transition: .3s top;
    z-index: 999;
}

.search.open {
    top: 0 !important;
}

.search input {
    width: calc(100% - 55px);
    padding: 5px 28px;
    font-size: 16px;
    height: 29px;
    margin: 14px auto;
    background-color: transparent;
    color: #fefefe;
    border: none;
    outline: none;
}

@media only screen and (max-width: 1180px) {
    .search {
        position: fixed;
    }

    .search input {
        height: 42px;
    }
}
</style>
