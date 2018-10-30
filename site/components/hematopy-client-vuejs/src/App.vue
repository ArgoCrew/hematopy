<template>
  <div id="app">
    <section class="hero is-white is-fullheight">
      <div class="hero-body">
        <div class="container">
          <!-- <hematopy-form></hematopy-form> -->
          <FileUpload></FileUpload>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import HematopyForm from './components/HematopyForm.vue'
import FileUpload from './components/FileUpload.vue'

export default {
  name: 'app',
  components: {
    HematopyForm,
    FileUpload
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Noto+Sans:400,700');
@import url('https://fonts.googleapis.com/css?family=Karla');
@import url('https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css');
// @import '../node_modules/bulma/css/bulma.min.css';

#app {
  font-family: 'Karla', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
