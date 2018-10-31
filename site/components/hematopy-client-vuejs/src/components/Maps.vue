<template>
  <div>
    <input ref="autocomplete" 
    placeholder="Informe o endereço do hospital" 
    class="search-location"
    onfocus="value = ''" 
    type="text" />
  </div>
</template>
<script>
export default {
  name: 'Maps',
  created() {
    this.setGoogleApiPlace()
  },
  mounted() {
    setTimeout(() => {
      this.setConfigGoogleApi()
    }, 500)
  },
  methods: {
    setGoogleApiPlace () {
      return new Promise(resolve => {
        let recaptchaScript = document.createElement('script')
        recaptchaScript.setAttribute('src', 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDnOXTF1Mzm7OJWbWlP4AdhNvEfLCiX6-w&libraries=places')
        document.head.appendChild(recaptchaScript)
        resolve(true)
      });
    },
    setConfigGoogleApi () {
      this.autocomplete = new google.maps.places.Autocomplete(
        (this.$refs.autocomplete),
        {types: ['hospital']}
      );
    }
  }
}
</script>
