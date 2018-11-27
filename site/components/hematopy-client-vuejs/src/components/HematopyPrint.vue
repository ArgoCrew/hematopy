<template>
    <div class="print">
        <div class="print-content">
          <div class="image">
            <figure class="image is-128x128 has-image-centered">
                <img :src="file.base64" class="is-rounded" alt="Imagem do paciente">
            </figure>
            <div class="recipient-name title">
                <h2>{{ this.recipient.recipientName }}</h2>
            </div>
            <div class="recipient-typeblood title">
                <h4>{{ this.recipient.recipientTypeBlood }}</h4>
            </div>
          </div>
        </div>
        <div class="navegation-buttons">
            <a class="button"
                @click.prevent="$emit('printrecipient')">
                    Imprimir
            </a>
        </div>
    </div>
</template>
<script>
export default {
  name: "HematopyPrint",
  props: ["recipient"],
  data() {
    return {
      file: {
        name: "",
        base64: ""
      }
    };
  },
  mounted() {
    this.file.name = this.recipient.file.name;
    this.file.base64 = this.recipient.file.base64;
  }
};
</script>
<style lang="scss">
h1, h2 {
    text-transform: uppercase;
}


.print {
    border: 1px solid black;
    width: 100%;
    padding: 2em;
    .print-content { 
        padding: 1em;
    }
}
</style>

