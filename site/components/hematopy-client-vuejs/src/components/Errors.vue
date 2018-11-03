<template>
  <div class="errors">
    <span
    v-for="(error, index) in errors"
    :key="index">
      {{ error }}
    </span>
  </div>
</template>
<script>
export default {
  name: 'Errors',
  props: ['errors']
}
</script>
