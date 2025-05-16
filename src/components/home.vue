<template>
    <div class="container" v-for="book in allBooks">
        <RouterLink :to="{path: '/books/' + book[3]}">
            <img v-bind:src="retrieveCover(book)">
        </RouterLink>
    </div>
</template>

<script>
import axios from 'axios';
import Book from './book.vue';

export default {
    name:'HomeView',
    data() {
        return {
            allBooks:{},
            path: 'http://127.0.0.1:5000/books'
        }
    },
    mounted() {
        let _this = this;
        axios.get(_this.path, {
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
        }).then(
            (response) => {
                _this.allBooks = response.data;
            },
            (error) => {
                console.log(error);
            }
        );
    },
    methods: {
        retrieveCover(book) {
            return "/" + book[0];
        },
    },
    components: {
      'Book':Book
    }
}
</script>

<style>

.container {
    display:inline-grid;
}

img {
    height: 260px;
    width: 175px;
    margin: 15px 0 15px 15px;
    cursor: pointer;
}

</style>