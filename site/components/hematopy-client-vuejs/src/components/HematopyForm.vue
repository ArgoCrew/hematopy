<template>
 <div class="container">
     <div class="columns">
      <div class="column">
        <input class="input" type="text" id="recipient-name" name="recipient-name" placeholder="Informe o nome do paciente"
          v-on:keyup.enter="formValidate"
          v-model="recipient.recipientName">
      </div>    
    </div>
    <div class="columns">
      <div class="column">
        <div class="select">
          <select id="recipient-blood-type" name="recipient-blood-type"
            v-model="recipient.recipientTypeBlood">
            <option disabled value="">Escolha o tipo sanguíneo</option>
            <option
              v-for="(type, index) in recipientTypeBloodList"
              :key="index">
              {{ type }}
            </option>
          </select>
        </div>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <Errors
          :errors="errors"
          v-if="true"></Errors>
      </div>
    </div>
 </div>
</template>

<script>
import Vue from 'vue'
import Api from '@/services/Api'
import Errors from '@/components/Errors.vue'

export default {
  name: 'HematopyForm',
  props: ['step','recipient'],
  data () {
    return {
      recipientName: '',
      recipientTypeBloodList: ['O+', 'A+', 'B+', 'AB+', 'O-', 'A-', 'B-', 'AB-'],
      errors: []
    }
  },
  methods: {
    formValidate () {
      const model = { ...this.recipient }
      if(model.recipientName.length <= 0){ this.setError('Nome do paciente é obrigatório') }
      if(model.recipientTypeBlood.length <= 0) { this.setError('Tipo de sangue do paciente é obrigatório') }
      if(this.errors.length === 0) { this.setRecipient() }
    },
    setRecipient () {
      this.$emit('nextstep')
    },
    setError (error) {
      this.errors.push(error)
    }
  },
  components: {
    Errors
  }
}
</script>
