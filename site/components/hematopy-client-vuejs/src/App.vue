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
                @setfile="setFile"
                :file="recipient.file"
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
              <HematopyPrint
                :recipient='recipient'
                v-if="step === 3"></HematopyPrint>
            </div>
          </div>
           <div class="columns">
            <div class="column">
              <NavegationButtons
                @nextstep="nextStep"
                @previousstep="previousStep"
                :file="recipient.file"
                :step="step"
                v-if="step !== 3">
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
import NavegationButtons from './components/NavegationButtons.vue'
import HematopyPrint from './components/HematopyPrint'

export default {
  name: 'app',
  data () {
    return {
      step: 0,
      recipient: {
        file: {
          name: '',
          base64: ''
        },
        recipientName: '',
        recipientTypeBlood: ''
      }
    }
  },
  methods: {
    nextStep () {
      if (this.step <= 2) { this.step++ }
    },
    previousStep () {
      if (this.step > 0 && this.step <= 2) { this.step-- }
    },
    setFile (params) {
      this.recipient.file.name = params.name
      this.recipient.file.base64 = params.base64 
    }
  },
  components: {
    FileUpload,
    HematopyForm,
    Maps,
    NavegationButtons,
    HematopyPrint
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
