<template>
    <div class="indicator">
        <div class="item">
            <BootstrapIcon icon="pencil" class="icon" />
            <span>{{ data.words }} Word</span>
        </div>

        <div class="item">
            <span>{{ data.characters }} Character</span>
        </div>
    </div>
</template>

<script>
export default {
    name: 'IndicatorComponent',
    props: {
        data: {
            type: Object,
            required: true
        }
    }
}
</script>

<style>
.indicator {
    position: fixed;
    bottom: 0;
    right: 0;
    background-color: var(--background-default);
    border-left: 1px solid #363636;
    border-top: 1px solid #363636;
    border-top-left-radius: 10px;
    padding: 8px;
    display: flex;
    justify-content: center;
    color: #9f9f9f;
    font-family: 'Courier New', Courier, monospace
}

.indicator .item .icon {
    font-size: 16px;
    margin-right: 10px;
    margin-top: -2px;
}

.indicator .item {
    margin: 0px 10px;
    text-align: center;
    font-size: 14px;
}

@media only screen and (max-width: 1180px) {
    .indicator {
        display: none;
    }
}
</style>
