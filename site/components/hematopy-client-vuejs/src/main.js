import Vue from 'vue'
import App from './App.vue'
import 'bulma/css/bulma.min.css'
import './assets/fonts/font-awesome/css/font-awesome.min.css'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDnOXTF1Mzm7OJWbWlP4AdhNvEfLCiX6-w',
    libraries: 'places'
  }
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
