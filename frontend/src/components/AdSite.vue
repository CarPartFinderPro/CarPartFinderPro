<template>
  <div id="app">
    <HeaderComponent />
    <div>
      <VueSidebarMenuAkahon />
    </div>
  </div>
  <div class="ad-site">
    <h1>{{ adTitle }}</h1>
    <div class="ad-image-container">
      <img src="../src/assets/seats.jpg" alt="seats">
    </div>
    <div class="ad-main-info">
      <h1>Fotele samochodowe</h1>
      <p>Marka:{{ adBrand }}</p>
      <p>Model:{{ adModel }}</p>
      <p>Rok:{{ adYear }}</p>
      <h2><strong>Cena: Milion dolarów (głównie w złotówkach)</strong> {{ adPrice }}</h2>
    </div>
    <div class="buy-now-btn">
    <button @click="buyNow">Kup Teraz</button>
  </div>
    <div class="ad-seller-info">
      <h2>Informacje o sprzedawcy:</h2>
      <p><strong>Imię:</strong> {{ sellerName }}</p>
      <p><strong>Telefon:</strong> {{ sellerPhone }}</p>
      <p><strong>Miejscowość:</strong> {{ sellerCity }}</p>
    </div>
    <div class="ad-details">
      <h2>Szczegóły:</h2>
      <p><strong>Kategoria:</strong> {{ adCategory }}</p>
      <p><strong>Marka:</strong> {{ adBrand }}</p>
      <p><strong>Model:</strong> {{ adModel }}</p>
      <p><strong>Rok produkcji:</strong> {{ adYear }}</p>
      <p><strong>Kraj pochodzenia:</strong> {{ adCountry }}</p>
      <p><strong>OEM (producent oryginalnego wyposażenia):</strong> {{ adOEM }}</p>
    </div>
  </div>
</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import HeaderComponent from "./components/HeaderComponent.vue";
export default {
  name: "AdSite",
  components: {
    VueSidebarMenuAkahon,
    HeaderComponent
  },
  props: {
    adTitle: String,
    adDescription: String,
    adBrand: String,
    adModel: String,
    adYear: Number,
    adPrice: String,
    sellerName: String,
    sellerEmail: String,
    sellerPhone: String,
  },
  methods: {
    buyNow() {
      // logika dla kliknięcia przycisku "Kup Teraz"
    }
  }
};
</script>

<style scoped>

.ad-main-info{
  margin-top: 50px;
  text-align: center;
}

.ad-main-info p {
  display: inline-block;
  margin-right: 20px;
}

.ad-image-container {
  float: left;
  margin-left: 100px;
}

.ad-details {
  margin-top: 100px;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f5f5f5;
  text-align: left;
}
.ad-seller-info {
  margin-left: 800px;
  margin-right: 100px;
  margin-top: 50px;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f5f5f5;
  text-align: left;
}

.ad-details h2,
.ad-seller-info h2 {
  margin-top: 0;
}

.buy-now-btn {
  margin-left: 1300px;
  margin-right: 220px;
  color: white;
  background-color: #ca2519;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.buy-now-btn:hover {
  background-color: #d4660b;
}
</style>