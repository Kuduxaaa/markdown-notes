<template>
    <div class="sidebar-item">
        <router-link :to="{ name: 'Post', params: { id: id } }">
            <div class="item">
                <p class="truncate">
                    <BootstrapIcon class="icon" :icon="icon" size="lg" /> {{ name }}
                </p>
            </div>
        </router-link>
    </div>
</template>


<script>
export default {
    name: 'SidebarItemComponent',
    props: {
        name: {
            type: String,
            required: true
        },

        id: {
            type: Number,
            required: true
        },

        icon: {
            type: String,
            required: false,
            default: 'file-text'
        }
    }
}
</script>

<style scoped>
.sidebar-item {
    width: 100%;
    font-size: 18px;
}

.item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 24px;
    margin-top: 7px;
    border-radius: 8px;
    transition: .3s background;
}

.item:hover,
.item.active {
    background-color: #393939;
    color: #dedede;
}

a {
    text-decoration: none;
    color: #9e9e9e;
}

.icon {
    margin-right: 12px;
}

.truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}


@media only screen and (max-width: 1180px) {
    .sidebar-item {
        font-size: 14px;
    }
}
</style>
