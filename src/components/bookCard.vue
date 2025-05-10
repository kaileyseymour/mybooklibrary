<template>
  <div>
    <h2>{{ cover }}</h2>
  </div>
</template>
  
<script>
  
export default {
    name: 'bookCard',
    props:['cover','title','author','isbn', 'myRating', 'averageRating', 'publisher','length','publishedYear','dateRead','myReview'],
    data: function() {
        return {

        }
    },
    created:function(){
    },
    methods:{
    
    },
    mounted:function(){

    },
    filters: {
    },
    components: {
    },
};
</script>
  
<style>
h2 {
    color: pink;
}
/* .bookCard{
    margin-top:10px;
    background:white;
    border-radius: 5px;
    height: auto;
    box-shadow: 0px 0px 7px 0px rgba(0, 0, 0, 1.0) !important;
} */
      
#overlay:hover .overlay{
    opacity: 1;
}
  
.overlay {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    height: 100%;
    width: 100%;
    opacity: 0;
    transition: .5s ease;
    box-shadow:inset 0 0 0 2000px rgba(0, 0, 0, 0.5);
    cursor: pointer;
}
</style>