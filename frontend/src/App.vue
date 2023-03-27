<template>
  <div id="app">
    <HeaderComponent />
    <CarPartList />
    <div>
      <VueSidebarMenuAkahon />
    </div>
  </div>
</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import HeaderComponent from "./components/HeaderComponent.vue";
import CarPartList from "./components/CarPartList.vue";

export default {
  name: "App",
  components: {
    VueSidebarMenuAkahon,
    HeaderComponent,
    CarPartList
  },
  data() {
    return {};
  },
};
</script>