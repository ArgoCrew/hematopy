<template>
  <div id="app">
    <section class="hero is-white is-fullheight">
      <div class="hero-body">
        <div class="container">
          <hematopy-form></hematopy-form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Vue from 'vue'
import HematopyForm from './components/HematopyForm.vue'

export default {
  name: 'app',
  components: {
    HematopyForm
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Noto+Sans:400,700');
@import url('https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css');

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
