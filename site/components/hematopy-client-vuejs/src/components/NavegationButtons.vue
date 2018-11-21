<template>
  <div class="navegation-buttons">
    <a class="button"
      @click.prevent="$emit('previousstep')"
      v-if="step !== 0"
      >
      Voltar
    </a>
    <a class="button is-info"
      @click.prevent="$emit('nextstep')"
      v-if="this.file.name"
      >
      Continuar
    </a>
  </div>
</template>
<script>
export default {
  name: 'NavegationButtons',
  props: ['step', 'file']
}
</script>
<style lang="scss" scoped>
  .navegation-buttons {
    > .button {
      margin: 10px;
      text-transform: uppercase;
      font-weight: 500;
    }
  }
</style>
