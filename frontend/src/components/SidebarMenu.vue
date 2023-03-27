<!-- <template>
  <div>
      <VueSidebarMenuAkahon />
  </div>
</template> -->

<template>
  <div>
    <ul>
      <li>
        <router-link to="/">Strona główna</router-link>
      </li>
      <li>
        <router-link to="/users">Użytkownicy</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
  import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
  
  export default {
    name: 'SidebarMenu',
    components: {VueSidebarMenuAkahon},
    data() {
      return {}
    }
  }
</script>