<script>
    let counter = $state(0);
    let press = $state(false);
    let hover = $state(false);

    const handleClick = () => {
        counter += 1;
        // ! Вызываем python-функцию с именем "button_counter"
        // ! и передаем ей значение счётчика
        // @ts-ignore
        py_call("button_counter", counter);
    }
</script>


<div id="py-button">
    <div>Counter: {counter}</div>
    <button class:btn-hover={hover} class="btn" class:btn-click={hover && press}
        onclick={handleClick}
        onmousedown={() => {press = true}}
        onmouseup={() => {press = false}}
        onmouseenter={() => {hover = true}}
        onmouseleave={() => {hover = false; press = false}}
    >Py Button</button>
</div>


<style>
    #py-button {
        padding: 20px 0;
    }
    
    .btn {
        background-color: #c30;
        color: white;
        padding: 14px 20px;
        border: none;
        cursor: pointer;
        text-shadow: 0 0 10px black;
        border-radius: 5px;
        box-shadow: 0 0 0;
        transition: all .1s ease;
    }

    .btn-hover {
        box-shadow: 0 5px 5px black;
    }

    .btn-click {
        box-shadow: 0 3px 3px black;
    }

    #py-button div {
        padding: 10px 0;
        color: white;
    }
</style>