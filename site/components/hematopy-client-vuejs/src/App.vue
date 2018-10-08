<template>
  <div id="app">
    <hematopy-form :questions="questions"/>
  </div>
</template>

<script>
import HematopyForm from './components/HematopyForm.vue'
import questions from './assets/questions'

export default {
  name: 'app',
  components: {
    HematopyForm
  },
  data () {
    return {
      questions,
      model: { }
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
