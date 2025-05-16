<template>
    <div class="bookContainer">
        <div class="imageContainer">
            <img id="singleBook" v-bind:src="'/' + image">

            <div class="minorDetails">
                <h5>Publisher Details</h5>
                <h6>Published by {{ publisher }}</h6>
                <h6>Published in {{ yearPublished }}</h6>
                <h6>{{ numOfPages }} pages</h6>
            </div>
        </div>
        <div class="majorDetails">
            <h2><i>{{ title }}</i> by {{ author }}</h2>
            <h3>Date Read: {{ dateRead }}</h3>
            <div class="ratings">
                <div v-if="myRating != 0">
                    <h3 id="myRating">
                        My Rating: {{ myRating }}
                        <i class="fas fa-star"></i>
                    </h3>
                </div>
                <h3>
                    Average Rating: {{ averageRating }}
                    <i class="fas fa-star"></i>
                </h3>
            </div>
            <div v-if="myReview != null">
                <div class="review">
                    <h4>My Review:</h4>
                    <div v-html="myReview"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';


export default {
    name:'BookView',
    props:['isbn'],
    data() {
        return {
            book:undefined,
            image:'',
            title:'',
            author:'',
            myRating:'',
            averageRating:'',
            publisher:'',
            numOfPages:undefined,
            yearPublished:undefined,
            dateRead:undefined,
            myReview:''
        }
    },
    mounted() {
        let _this = this;
        let path = 'http://127.0.0.1:5000/books/';
        if(_this.isbn.startsWith('0')) {
            path += '"' + _this.isbn + '"';
        } else {
            path += _this.isbn;
        }

        axios.get(path, {
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
        }).then(
            (response) => {
                _this.book = response.data[0];

                //assign all attributes
                _this.image = _this.book[0];
                _this.title = _this.book[1];
                _this.author = _this.book[2];
                _this.myRating = _this.book[4];
                _this.averageRating = _this.book[5];
                _this.publisher = _this.book[6];
                _this.numOfPages = _this.book[7];
                _this.yearPublished = _this.book[8];
                _this.dateRead = _this.book[9];
                _this.myReview = _this.book[12];
            },
            (error) => {
                console.log(error);
            }
        );
    },
    methods: {

    },
    components: {
      
    }
}
</script>

<style>
.bookContainer {
    display: grid;
    grid-template-columns: 1fr 3fr;
    gap: 10px;
    padding: 10px;
}

.imageContainer {
    grid-row-start: 1;
    grid-row-end: 5;
}

.majorDetails {
    grid-column-start: 2;
    grid-column-end: 4;
}

.ratings {
    grid-column-start: 2;
    grid-column-end: 4;

    display: inline-flex;
}

.review {
    margin-left: 5px;
    grid-column-start: 2;
    grid-column-end: 4;
    grid-row-start: 3;
    grid-row-end: 5;

    text-align: bottom;
}

.minorDetails {
    margin-left: 5px;
    color: gray;
}

h2, h3 {
    margin: 5px;
}

h4 {
    margin-top: 25px;
}

h5, h6 {
    margin: 0px;
}

h5 {
    text-decoration-line: underline;
}

#singleBook {
    margin-left: 5px;
    height: 275px;
    width: 200px;
}

#myRating {
    padding-right: 80px;
}
</style>