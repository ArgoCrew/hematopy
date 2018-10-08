import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faBolt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import 'bulma/css/bulma.min.css'

library.add(faBolt)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
