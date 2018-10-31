<template>
  <div id="app">
    <section class="hero is-white is-fullheight">
      <div class="hero-body">
        <div class="container">
          <div class="columns">
            <div class="column">
              <FileUpload
                @nextstep="nextStep"
                @previousstep="previousStep"
                @setfilename="setFileName"
                :file="file"
                v-if="step === 0">
              </FileUpload>
            </div>
          </div>
          <div class="columns">
            <div class="column">
              <HematopyForm
                @nextstep="nextStep"
                @previousstep="previousStep"
                :recipient="recipient"
                :step="step"
                v-if="step === 1">
              </HematopyForm>
            </div>
          </div>
          <div class="columns">
            <div class="column">
              <Maps
                v-if="step === 2">
              </Maps>
            </div>
          </div>
           <div class="columns">
            <div class="column">
              <NavegationButtons
                @nextstep="nextStep"
                @previousstep="previousStep"
                :file="file"
                :step="step">
              </NavegationButtons>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import FileUpload from './components/FileUpload.vue'
import HematopyForm from './components/HematopyForm.vue'
import Maps from './components/Maps.vue'
import NavegationButtons from './components/NavegationButtons.vue';

export default {
  name: 'app',
  data () {
    return {
      step: 0,
      file: {
        name: '',
        urlBase64: ''
      },
      recipient: {
        recipientName: '',
        recipientTypeBlood: ''
      }
    }
  },
  methods: {
    nextStep () {
      if(this.step <= 2) { this.step++ }
    },
    previousStep () {
      if(this.step > 0 && this.step <= 2) { this.step-- }
    },
    setFileName (params) {
      this.file.name = params
    }
  },
  components: {
    FileUpload,
    HematopyForm,
    Maps,
    NavegationButtons
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Lato');
@import url('https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css');

#app {
  font-family: 'Lato', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
