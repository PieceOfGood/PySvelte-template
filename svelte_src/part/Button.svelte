<script>
    import { createEventDispatcher } from 'svelte';
    export let name = "";
    export let width = "auto";
    export let height = "36px";
    export let title = "";

    const dispatch = createEventDispatcher();
    let press = false;
    let hover = false;
</script>


<button class:btn-hover={hover} class="btn" class:btn-click={hover && press}
    title={title}
    style="width: {width}; height: {height}"
    on:click={() => dispatch("click")}
    on:mousedown={() => {press = true}}
    on:mouseup={() => {press = false}}
    on:mouseenter={() => {hover = true}}
    on:mouseleave={() => {hover = false; press = false}}
>
    { @html name }
    <slot name="icon"></slot>
</button>


<style>    
    .btn {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #c30;
        color: white;
        padding: 10px 15px;
        border: none;
        cursor: pointer;
        text-shadow: 0 0 10px black;
        border-radius: 5px;
        box-shadow: none;
        transition: all .1s ease;
    }

    .btn-hover {
        box-shadow: 0 5px 5px black;
        z-index: 1;
    }

    .btn-click {
        box-shadow: 0 3px 3px black;
    }
</style>
