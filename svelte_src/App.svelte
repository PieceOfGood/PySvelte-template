<script>
	import PyButton from "./part/PyButton.svelte";
	export let name;

	function navigate(event) {
		// ? Если это событие кнопки мыши:
		// ?   * x1(3) - навигация назад
		// ?   * x2(4) - навигация вперёд
		// ? предотвращаем его выполнение
		
		if ([3, 4].some((el) => el === event.button)) {
			event.preventDefault();
			event.stopPropagation();
			console.log("Preven navigate!");
		}
	}
</script>


<svelte:window on:mousedown={navigate} on:mouseup={navigate}/>


<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	
	<PyButton />
</main>


<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
