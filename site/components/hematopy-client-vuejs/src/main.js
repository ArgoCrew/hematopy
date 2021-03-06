import Vue from 'vue'
import App from './App.vue'
import './assets/fonts/font-awesome/css/font-awesome.min.css'
import * as VueGoogleMaps from 'vue2-google-maps'

require('./assets/sass/styles.scss')

Vue.use(VueGoogleMaps, {
  load: {
    key: process.env.VUE_APP_GOOGLE_PLACE_KEY,
    libraries: 'places'
  }
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
