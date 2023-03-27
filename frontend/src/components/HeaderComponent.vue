<template>
  <header class="header">
    <h1 class="title">CarPartFinder</h1>
    <!-- <div class="logo-container">
      <img src="../assets/logo_header.png" alt="Logo" class="logo" />
    </div> -->
  </header>
</template>

<script>
export default {
  name: "HeaderComponent",
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  height: 60px;
  background-color: #11101d;
  padding: 0;
  margin: 0;
  position: relative;
}

/* .logo-container {
  display: flex;
  align-items: center;
  height: 100%;
  padding: 0;
  margin: 0;
} */

/* .logo {
  height: 100%;
  margin: 0;
} */

.title {
  font-size: 30px;
  font-weight: bold;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  color: #fff;
}
</style>