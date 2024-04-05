import { createApp } from 'vue'
import { SnackbarService, Vue3Snackbar } from "vue3-snackbar";

import mitt from 'mitt';
import App from './App.vue'

import '@/assets/css/app.css'
import 'highlight.js/styles/monokai.css';
import 'github-markdown-css/github-markdown.css';
import 'vue3-snackbar/dist/style.css';

import BootstrapIcon from '@dvuckovic/vue3-bootstrap-icons';
import Markdown from 'vue3-markdown-it';
import Posts from './api';
import router from './router';

const app = createApp(App);
const posts = new Posts();
const emitter = mitt();

app.config.globalProperties.$posts = posts;
app.config.globalProperties.emitter = emitter;

app.use(router);
app.use(SnackbarService);
app.use(Markdown);

app.component('BootstrapIcon', BootstrapIcon);
app.component("vue3-snackbar", Vue3Snackbar);

app.mount('#app');
