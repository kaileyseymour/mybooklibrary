<template>
  <!-- the main MBMS view when card is toggled  -->
  <div id="mbms" class="page-container">
    <div class="container">
      <h3 id="mbms-header" tabindex="-1" style="color: black !important;"><b>MEMORIAL BENEFITS MANAGEMENT SYSTEM</b></h3>
      <div class="columns">
        <div class="column is-one-third">
              <a id="maplink-external" aria-label="CeRRT Application Image" :href="MBMSLinks['CeRRT'].image_link" target="_blank" tabindex="0"><portlet :title="'CeRRT'" :color="'va-blue'" :image="'MAP_thumbs_0000_Layer-21.png'">
              </portlet></a>
              <div class="columns links">
                <div class="column is-one-half">
                 <div v-html="MBMSLinks['CeRRT'].links_html"></div>
                </div>
              </div>
        </div>
        <div class="column is-one-third">
              <a id="maplink-external" aria-label="CaMEO Application Image" :href="MBMSLinks['CaMEO'].image_link" target="_blank" tabindex="0"><portlet :title="'CaMEO'" :color="'va-blue'" :image="'AdobeStock_292770500_Chattanooga.jpeg'">
              </portlet></a>
              <div class="columns links">
                <div class="column is-one-half">
                 <div v-html="MBMSLinks['CaMEO'].links_html"></div>
                </div>
              </div>
        </div>
        <div class="column is-one-third">
          <a id="maplink-external" aria-label="MBMS Documents Application Image" :href="MBMSLinks['MBMS Documents'].image_link" target="_blank" tabindex="0"><portlet :title="'MBMS Documents'" :color="'va-blue'" :image="'MAP_thumbs_0018_Layer-7.png'">
          </portlet></a>
          <div class="columns links">
            <div class="column is-one-half">
             <div v-html="MBMSLinks['MBMS Documents'].links_html"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="columns">

        <!-- user guide tile -->
        <div class="column is-one-third">
          <portlet 
            ariaRole="link"
            tabindex="0"
            :sectionOpen="openComponent === userguide ? true : false" 
            :title="'MBMS User Guide'" 
            :color="'va-blue'" 
            :image="'MAP_thumbs_0023_Layer-3.png'"
            @keyup.enter="showComponent(userguide)"
            @click="showComponent(userguide)"
          >
          </portlet>
          <div class="columns links">
            <div class="column is-one-half">
             <div v-html="MBMSLinks['MBMS User Guide'].links_html"></div>
            </div>
          </div>
        </div>
        <div class="column is-one-third">
          <!-- selecting image will pop-up modal-->
          <div aria-label="MBMS Training Sandbox Link" tabindex="0" @click="confirmTrainingSwal()">
            <portlet :title="'MBMS Training Sandbox'" :color="'va-blue'" :image="'Training Sandbox Photo.jpg'"></portlet>
          </div>
          <div class="columns links">
            <div class="column is-one-half">
              <div v-html="MBMSLinks['MBMS Training Sandbox'].links_html"></div>
            </div>
          </div>
        </div>
        <div class="column is-one-third">
          <div v-if="placeholderTile.title">
            <a :href="placeholderTile.image_link" target="_blank"><portlet :title="placeholderTile.title" :color="'va-blue'" :image="'MAP_thumbs_0017_Layer-8.png'">
            </portlet></a>
            <div class="columns links">
              <div class="column is-one-half">
                  <div v-html="placeholderTile.links_html"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- when user guide tile is open, needs to open as a new component below -->
    <div>
      <br/>
      <!-- invisible header to scroll to when component opens -->
      <h3 id="userguide-open-component" class="item-hidden" tabindex="-1">MBMS User Guide section</h3>
      <transition name="fade">
        <keep-alive>
        <component tabindex='0' :is="openComponent"/>
        </keep-alive>
      </transition>
    </div>

  </div>
 </template>
 
 <script>
 
 import portlet from '../components/ui/portlet.vue'
 import userguide from '../views/userguide.vue'
 import { event } from 'vue-gtag'
 import Swal from 'sweetalert2'

 export default {
   name: 'home',
    data: function () {
     return {
       releasenotes:[],
       announcements:[],
       placeholderTile: {},
       modalLinks: {},
       userguide: 'userguide',
       openComponent: null
     }
   },
   created:function(){
     const _this = this;
 
     let links = [..._this.$store.state.MBMSLinks];
     let formattedLinksArr = {};
 
     for (let i = 0; i < links.length; i++) {
      //set modal pop up links
      if(links[i].title == "Modal Links") {
        _this.modalLinks = JSON.parse(links[i].links_html);
        continue;
      }
      if (!links[i].type.includes("Placeholder")) {
        formattedLinksArr[links[i].title] = links[i];
      } else { // set placeholder tile
        this.placeholderTile = links[i];
      }
     }
     _this.MBMSLinks = formattedLinksArr;
     
   },
   mounted:function(){    
    // Get all links from the html. If they have an id that starts with "maplink"
    // then add them to the appropriate array.
    let downloadLinks = [];
    let externalLinks = [];
    let MAPLinkElements = document.getElementsByTagName("a");
    for (let i = 0; i < MAPLinkElements.length; i++) {
      if (MAPLinkElements[i].id.lastIndexOf("maplink-", 0) === 0) {
        if (MAPLinkElements[i].id.endsWith("download")) {
          downloadLinks.push(MAPLinkElements[i]);
        } else if (MAPLinkElements[i].id.endsWith("external")) {
          externalLinks.push(MAPLinkElements[i]);
        }
      }
    }

    // Add GA event tracking to the links from the html
    for (let i = 0; i < downloadLinks.length; i++) {
      downloadLinks[i].addEventListener('click', function(e){
        event('Downloads', {'downloaded_name': downloadLinks[i].innerHTML, 'downloaded_url': downloadLinks[i].href, 'downloaded_label': downloadLinks[i].ariaLabel});
      });
    } 
    
    for (let i = 0; i < externalLinks.length; i++) {
      externalLinks[i].addEventListener('click', function(e){
        event('External_Click', {'external_text': externalLinks[i].innerText, 'external_url': externalLinks[i].href, 'external_label': externalLinks[i].ariaLabel});
      });
    } 
   },
   methods:{
    showComponent: function(component) {
       this.openComponent = component;
       let header = document.getElementById("userguide-open-component");
       setTimeout(function() {
        header.scrollIntoView({ behavior: "smooth" });
        header.setAttribute('tabindex', '0');
        header.focus()
        header.setAttribute('tabindex', '-1');
        setTimeout(function(){
          header.setAttribute('tabindex', '-1');
        },400)
       }, 300);
       event('Section_Click', {'section_name': component});
     },
    //open MBMS Training Sandbox pop-up modal
    confirmTrainingSwal: function() {
      let _this = this;
      let sandbox = _this.modalLinks['salesforce_sandbox'];
      let trainingRequestForm = _this.modalLinks['training_request_form'];
      Swal.fire({
        html: `Reminder: Do not enter any Personally Identifiable Information (PII) into the Training Environment. <br><br> If you do not have access to the Training Environment, please select and fill out the <a target='_blank' href="${trainingRequestForm}">Training Request Form</a>. <br><br> Click <b>OK</b> to continue to the MBMS Training Environment.`,
        icon: "warning",
        showCancelButton: true,
        cancelButtonColor:'#7D7D7D',
        confirmButtonColor:'#3185D6',
        iconColor: '#CD670E',
        confirmButtonText: 'OK'
      }).then((result) => {
        if (result.value) {
          window.open(sandbox, "_blank");
        }
      });
    }
   },
   components: {
     'portlet': portlet,
     'userguide': userguide
   }
 }
 </script>
 
 
 <style lang="scss" scoped>
 @import "../sass/variables.scss";

 .item-hidden {
  position: absolute !important;
  width: 90% !important;
  height: 0% !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0,0,0,0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}
 
 #mbms{
   background: $va-periwinkle;
   padding-bottom: 50px;
   padding-top: 50px;
   margin-top: 100px;
 }
 
 .links {
   color: black !important;
   margin-top: 10px;
   font-family: 'Source Sans Pro', sans-serif;
 }
 
 a{
   color: black !important;
 }
 
 a:hover{
     color: $va-blue;
   }
 
 .column {
   p {
     margin-left: 2px;
   }
   color: black;
 }

 </style>