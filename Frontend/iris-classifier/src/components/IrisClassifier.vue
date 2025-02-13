<template>
  <div class="container">
    <h2>Iris Flower Classification</h2>
    <form @submit.prevent="predict">
      <div v-for="(feature, index) in featureNames" :key="index" class="slider-container">
        <label :for="feature">{{ feature }}: {{ features[index].toFixed(1) }}</label>
        <input 
          type="range" 
          :min="featureRanges[index].min" 
          :max="featureRanges[index].max" 
          :step="featureRanges[index].step" 
          v-model.number="features[index]" 
          class="slider"
        />
      </div>
      <button type="submit">Predict</button>
    </form>
    <div v-if="prediction">
      <h3>Prediction: {{ prediction }}</h3>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      featureNames: [
        "Sepal Length (cm)",
        "Sepal Width (cm)",
        "Petal Length (cm)",
        "Petal Width (cm)",
      ],
      featureRanges: [
        { min: 4.0, max: 8.0, step: 0.1 },
        { min: 2.0, max: 4.5, step: 0.1 },
        { min: 1.0, max: 7.0, step: 0.1 },
        { min: 0.1, max: 2.5, step: 0.1 },
      ],
      features: [5.1, 3.5, 1.4, 0.2], // Default values
      prediction: null,
    };
  },
  methods: {
    async predict() {
      try {
        const payload = {
          features: [...this.features],  // Ensures it's properly structured
        };

        const response = await axios.post("http://127.0.0.1:5000/predict", payload, {
          headers: { "Content-Type": "application/json" } // Explicitly define JSON
        });

        this.prediction = response.data.prediction;
      } catch (error) {
        console.error("Error making prediction:", error);
      }
    },
  },
};
</script>

<style>
/* Centering the form */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  background-color: #1e1e1e;
  color: white;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 300px;
  background: #282c34;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
}

.slider-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.slider {
  width: 100%;
}

button {
  background-color: #28a745;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
}

button:hover {
  background-color: #218838;
}

/* Remove default margin and padding */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  background-color: #1e1e1e; /* Match dark theme */
  color: white;
  height: 100%;
  overflow: hidden;
}

</style>
