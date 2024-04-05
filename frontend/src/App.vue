<template>
    <div>
        <vue3-snackbar bottom right :duration="4000"></vue3-snackbar>
        <router-view />
    </div>
</template>

<script>
export default {
    name: 'App'
}
</script>
