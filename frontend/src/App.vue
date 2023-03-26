<template>
  <div id="app">
    <HeaderComponent />
    <div>
      <VueSidebarMenuAkahon />
    </div>
  </div>
</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import HeaderComponent from "./components/HeaderComponent.vue";

export default {
  name: "App",
  components: {
    VueSidebarMenuAkahon,
    HeaderComponent,
  },
  data() {
    return {};
  },
};
</script>

