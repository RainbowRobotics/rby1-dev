<template>
    <div class="content">
        <div class="content-container">
            <main class="main">
                <div class="vp-doc" flex flex-col items-center>
                    <!-- <h2 id="slogan" op90 font-normal p="t-10 b-2">
                        RB-Y1
                    </h2>
                    We developed a Dual-Arm Mobile Manipulator RB-Y1 to merge AI technology with our robot platforms. -->
                    <div w-full p-10>
                    </div>
                    <!-- <div w-full p-10>
                        <VPTeamMembers size="small" :members="teamMembers" />
                    </div> -->
                </div>
                <!-- <div style="display: flex; justify-content: center;">
                    <img src="../../assets/lineup.png" />
                </div> -->
            </main>
        </div>
        <div v-if="showPopup" id="popup" class="popup">
            <div class="popup-content">
                <span @click="closePopup" class="close">&times;</span>
                <Notice />
                <div class="popup-checkbox">
                    <input type="checkbox" v-model="dontShowForWeek" id="dont-show-checkbox" />
                    <label for="dont-show-checkbox">Don't show again for a week</label>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Notice from './notice.md' // Markdown 파일 경로
const showPopup = ref(false)
const dontShowForWeek = ref(false)

onMounted(() => {
    const lastPopupDate = localStorage.getItem('popupClosedDate')
    const oneWeekInMs = 7 * 24 * 60 * 60 * 1000

    if (!lastPopupDate || Date.now() - parseInt(lastPopupDate) > oneWeekInMs) {
        showPopup.value = true
    }
})

const closePopup = () => {
    if (dontShowForWeek.value) {
        localStorage.setItem('popupClosedDate', Date.now().toString())
    }
    showPopup.value = false
}
</script>

<style>
:root {
    /* Light mode colors */
    --popup-bg-color: rgba(0, 0, 0, 0.5);
    --popup-content-bg-color: #ffffff;
    --popup-close-color: #000000;
    --popup-border-radius: 12px;
    --popup-box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.dark {
    /* Dark mode colors */
    --popup-bg-color: rgba(0, 0, 0, 0.7);
    --popup-content-bg-color: #2c2c2c;
    --popup-close-color: #ffffff;
    --popup-border-radius: 12px;
    --popup-box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

/* Popup overlay */
.popup {
    display: flex;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: var(--popup-bg-color);
    align-items: center;
    justify-content: center;
    padding: 20px;
}

/* Popup content box */
.popup-content {
    background-color: var(--popup-content-bg-color);
    padding: 30px;
    width: 90%;
    max-width: 500px;
    border-radius: var(--popup-border-radius);
    box-shadow: var(--popup-box-shadow);
    position: relative;
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Markdown styling within the popup */
.popup-content h2 {
    margin-top: 0;
    color: var(--popup-close-color);
    font-size: 24px;
    font-weight: bold;
}

.popup-content p, .popup-content ul {
    margin-bottom: 1em;
}

.popup-content ul {
    padding-left: 20px;
}

.popup-content li {
    list-style-type: disc;
    margin-left: 20px;
}

/* Styling links to make them stand out */
.popup-content a {
    color: #1e90ff;
    text-decoration: underline;
    font-weight: bold;
}

/* Close button styling */
.close {
    position: absolute;
    top: 15px;
    right: 20px;
    font-size: 24px;
    cursor: pointer;
    color: var(--popup-close-color);
}

/* Checkbox styling */
.popup-checkbox {
    margin-top: 20px;
    display: flex;
    align-items: center;
}

.popup-checkbox input[type="checkbox"] {
    margin-right: 8px;
}
</style>