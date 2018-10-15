<template>
  <div>
    <h2>Search and add a pin</h2>
    <label>
      <gmap-autocomplete
        @place_changed="setPlace">
      </gmap-autocomplete>
      <button @click="addMarker">Add</button>
    </label>
    <br/>
  </div>  
</template>

<script>
export default {
  name: "GoogleMap",
  data() {
    return {
      places: [],
      currentPlace: null
    };
  },
  methods: {
    setPlace(place) {
      this.currentPlace = place;
    }
  }
};
</script>