import './main-app-global.css';
import { mount } from 'svelte';
import App from './App.svelte';


const app = mount(App, {
	target: document.getElementById('app'),
	props: {name: 'world'},
});

export default app;