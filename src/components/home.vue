<template>
    <div class="container" v-for="book in allBooks">
        <img v-bind:src="retrieveCover(book)">
    </div>
</template>

<script>
import axios from 'axios';
import BookCard from './bookCard.vue';

export default {
    name:'home',
    data() {
        return {
            allBooks:{},
        }
    },
    mounted() {
        let _this = this;
        const path = 'http://127.0.0.1:5000/books';
        axios.get(path, {
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
            return "src/images/" + book[0];
        }
    },
    components: {
      'BookCard':BookCard
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
}

</style>