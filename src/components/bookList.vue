<template>
<div class="portlet-list">
	<div :class="'header ' + color">
       <h2 class="section-title"> {{title}}</h2>
    </div>
   <figure v-if="image" class="image is-5by3 ">
    <img class="portimg" :src="image.src" :alt="image.alt">
   </figure>
    <div v-if="list.length > 0" class="content columns  is-multiline scroll">
        <item-column v-for="(item, i) in list" :key="'portlet-list-item-'+i" :item="item" :show="show"></item-column>
    </div>
    <div v-else class="content columns is-multiline ">
        <div class="column is-full">
             <span class="title">{{none}}</span>
        </div>
    </div>
</div>



</template>

<script>


import itemCol from './item-column.vue'

export default {
  name: 'card',
  props:['title','color','list','none','show','image'],
   data: function () {
    return {
      system:undefined,
      active:undefined,
    }
  },
  created:function(){
  },
  methods:{


  },
  mounted:function(){

             OverlayScrollbars(document.querySelectorAll(".scroll"), {
            className : "os-theme-dark os-"+this.color
          });

  },
  filters: {



  },
  components: {
      'item-column':itemCol
  }
}
</script>


<style lang="scss" scoped>
@import "../../sass/variables.scss";

.portlet-list{
   margin-top:$portlet-margin;
       padding-bottom:10px;
       background:white;
       border:2px solid white;
       border-radius: 0px;

    .header{
        padding:10px 20px;
        color:white;


        font-size:25px;
        @import "../../sass/colors.scss";
    }
    .portimg{
        padding:15px;
    }
		.section-title{
			font-size: 20px;
			font-weight: 800;
		}
    .content{
        padding: 15px;
        background-color:white;
        margin:0px;
         max-height: 500px;
    overflow: hidden;
    height: 370px;
        .title{
            font-weight: bold;
            font-size:16px;
        }

        .last-viewed{
            color:grey;
            display: block;
        }
        .list-item-column{
            margin:0px;
            padding-bottom: 1px;

            &:hover{
                cursor: pointer;
                background:$row-highlight;
            }
        }
        .icon-column{
            font-size:30px;
            max-width: 50px;

            i{
                padding:5px;
                color:white;
                border-radius: 25px;
                @import "../../sass/colors.scss";
            }
        }
    }
    @include box-shadow-standard();
}
</style>
