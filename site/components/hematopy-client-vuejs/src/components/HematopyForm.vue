<template>
    <section class="hero is-white is-fullheight">
      <div class="hero-body">
        <div class="container">
          <form action="">
            <input type="text" v-model="recipientImage">
            <input type="text" v-model="recipientName">
            <input type="text" v-model="recipientBloodType">
            <input type="text" v-model="locationAddressRegion">
            <input type="text" v-model="locationAddressLocality">
            <input type="text" v-model="locationAddressDistrict">
            <input type="text" v-model="locationAddressStreet">
            <input type="text" v-model="locationAddressNumber">
            <button>
              enviar
            </button>
          </form>
        </div>
      </div>
    </section>
</template>

<script>
export default {
  name: 'HematopyForm',
  props: ['questions']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
