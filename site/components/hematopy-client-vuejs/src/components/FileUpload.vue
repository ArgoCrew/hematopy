<template>
  <div class="file-upload">
    <div class="title">
      <h3 class="title">
        Foto do paciente
      </h3>
    </div>
    <div class="icon">
      <label for="file-input">
        <i class="fa fa-camera" aria-hidden="true"
          v-if="!fileExists"></i>
      </label>
    </div>
    <div class="action">
      <input id="file-input" type="file"
        @change="onFileChange" hidden/>
    </div>

    <div class="preview">
      <div class="image">
        <figure class="image is-128x128 has-image-centered">
          <img src="" class="is-rounded" alt="Imagem do paciente"
            v-show="fileExists">
          <figcaption class="figcaption">
            {{ file.name }}
          </figcaption>
        </figure>
      </div>
    </div>
    <div class="close-btn">
      <a class="button"
        @click.prevent="cancelViewFile"
        v-if="fileExists">Remover imagem</a>
    </div>

  </div>
</template>
<script>
export default {
  name: 'FileUpload',
  data () {
    return {
      file: {
        name: ''
      }
    }
  },
  methods: {
    onFileChange: function (e) {
      const file = e.target.files[0]
      this.previewFile()
      this.setFileName(file.name)
    },
    previewFile () {
      let reader = new FileReader()
      let preview = document.querySelector('img')
      const file = document.querySelector('input[type=file]').files[0]

      reader.addEventListener(
        'load',
        () => {
          let base64 = reader.result
          preview.src = base64
          this.setBase64(base64)
        },
        false
      )
      if (file) {
        reader.readAsDataURL(file)
      }
    },
    cancelViewFile (e) {
      let file = document.querySelector('input[type=file]').files[0]
      this.file.name = ''
    },
    setBase64 (_urlBase64) {
      this.file.urlBase64 = _urlBase64
    },
    setFileName (name) {
      this.file.name = name
    }
  },
  computed: {
    fileExists: function () {
      // `this` aponta para a instância Vue da variável `vm`
      return this.file.name.length > 0
    }
  }
}
</script>
<style lang="scss" scoped>
.file-upload {
  > .title {
    margin-bottom: 3em;
  }
  > .icon {
    font-size: 8em;
    > label {
      > i {
        cursor: pointer;
      }
    }
  }

  > .preview {
    > .image {
      > figure {
        > .figcaption {
          margin: 10px 0;
          text-transform: uppercase;
          color: #000000;
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
