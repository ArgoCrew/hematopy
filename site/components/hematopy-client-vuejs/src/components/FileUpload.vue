<template>
  <div class="file-upload">
    <div class="columns">
      <div class="column">
        <div class="title">
          <h3 class="title">
            Foto do paciente
          </h3>
        </div>
      </div>
    </div>
    <div class="columns" v-if="!fileExists">
      <div class="column">
        <div class="icon">
          <label for="file-input">
            <i class="fa fa-camera" aria-hidden="true"></i>
          </label>
        </div>
      </div>
    </div>
    <div class="action">
      <input id="file-input" type="file"
        @change="onFileChange" hidden/>
    </div>
    <div class="columns">
      <div class="column">
        <div class="preview">
          <div class="image">
            <figure class="image is-128x128 has-image-centered">
              <img :src="file.base64" class=" is-rounded" alt="Imagem do paciente"
                v-show="fileExists">
            </figure>
            <span>
              {{ file.name }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <div class="close-btn">
          <a class="button"
            @click.prevent="cancelViewFile"
            v-if="file.name">Remover imagem</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'FileUpload',
  props: ['file'],
  methods: {
    onFileChange: function (e) {
      const file = e.target.files[0]
      this.setFile(file)      
      this.previewFile()
    },
    previewFile () {
      let reader = new FileReader()
      let preview = document.querySelector('img')
      const file = document.querySelector('input[type=file]').files[0]

      reader.addEventListener(
        'load',
        () => {
          file.base64 = reader.result
          this.setFile(file)
        },
        false
      )
      if (file) {
        reader.readAsDataURL(file)
      }
    },
    cancelViewFile (e) {
      let file = document.querySelector('input[type=file]')
      file.value = ''
      this.file.name = ''
    },
    setFile (file) {
      this.file.name = file.name
      this.file.base64 = file.base64
      
      this.$emit('setfile', file)
    }
  },
  computed: {
    fileExists: function () {
      return this.file.name.length > 0
    }
  }
}
</script>
<style lang="scss" scoped>
.file-upload {
  > .columns {
    > .column {
    }
  }
  .columns {
    .column {
      > .title {
      }
      .icon {
        // padding: 0.1em 0;
        font-size: 3em;
        > label {
          > i {
            cursor: pointer;
          }
        }
      }
    }
  }

  > .close-btn {
    margin: 15px 0;
  }
}
.has-image-centered {
  margin-left: auto;
  margin-right: auto;
}
</style>
