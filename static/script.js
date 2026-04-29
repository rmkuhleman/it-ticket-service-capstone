window.addEventListener("DOMContentLoaded", function () {
    const categorySelect = document.getElementById("category");
    const subcategorySelect = document.getElementById("subcategory");
    const subcategoryMap = {
        "Hardware": ["Monitor", "Keyboard", "Mouse", "Laptop", "Desktop"],
        "Software": ["Login Issue", "Application Crash", "Installation Issue", "Permission Issue"],
        "Printer": ["Not Printing", "Offline", "Paper Jam", "Low Ink/Toner"],
        "Connectivity": ["Wi-Fi Issue", "No Internet", "Slow Connection", "VPN Issue"],
        "Other": ["General Issue"]
    };

    function populateSubcategories(selectedCategory, selectedSubcategory = "") {
        subcategorySelect.innerHTML = `<option value="">Select a subcategory</option>`;
        if (!selectedCategory || !subcategoryMap[selectedCategory]) return;
        subcategoryMap[selectedCategory].forEach(item => {
            const option = document.createElement("option");
            option.value = item;
            option.textContent = item;
            subcategorySelect.appendChild(option);
        });
        if (selectedSubcategory && subcategoryMap[selectedCategory].includes(selectedSubcategory)) {
            subcategorySelect.value = selectedSubcategory;
        }
    }

    function restoreSelections() {
        const savedCategory = sessionStorage.getItem("savedCategory") || "";
        const savedSubcategory = sessionStorage.getItem("savedSubcategory") || "";
        if (savedCategory) {
            categorySelect.value = savedCategory;
            populateSubcategories(savedCategory, savedSubcategory);
        } else {
            populateSubcategories("", "");
        }
    }

    function saveSelections() {
        sessionStorage.setItem("savedCategory", categorySelect.value);
        sessionStorage.setItem("savedSubcategory", subcategorySelect.value);
    }

    categorySelect.addEventListener("change", function () {
        populateSubcategories(categorySelect.value);
        saveSelections();
    });
    subcategorySelect.addEventListener("change", saveSelections);
    restoreSelections();
    window.addEventListener("pageshow", restoreSelections);

    const description = document.getElementById("description");
    const counter = document.getElementById("desc-counter");
    const tip = document.getElementById("desc-tip");
    if (description && counter) {
        const updateCounter = () => {
            const length = description.value.length;
            counter.textContent = `${length} / 3000`;
        };
        const savedDescription = sessionStorage.getItem("saved_description");
        if (savedDescription !== null) description.value = savedDescription;
        updateCounter();
        description.addEventListener("input", () => {
            sessionStorage.setItem("saved_description", description.value);
            updateCounter();
            const errorItem = document.querySelector(`.error-list li[data-field="description"]`);
            if (errorItem) errorItem.style.display = description.value.trim() ? "none" : "list-item";
            if (tip) tip.style.marginTop = "0.2em";
        });
    }

    const allInputs = document.querySelectorAll("input, select, textarea");
    allInputs.forEach(input => {
        const savedValue = sessionStorage.getItem("saved_" + input.name);
        if (savedValue !== null) input.value = savedValue;
        input.addEventListener("input", () => {
            sessionStorage.setItem("saved_" + input.name, input.value);
        });
    });

    const errorList = document.querySelector(".error-list");
    if (errorList) {
        const updateErrors = () => {
            const visibleErrors = JSON.parse(sessionStorage.getItem("visibleErrors") || "[]");
            errorList.querySelectorAll("li").forEach(li => {
                li.style.display = visibleErrors.includes(li.dataset.field) ? "list-item" : "none";
            });
        };

        const restoredErrors = [];
        errorList.querySelectorAll("li").forEach(li => {
            if (li.style.display !== "none") restoredErrors.push(li.dataset.field);
        });
        if (restoredErrors.length) sessionStorage.setItem("visibleErrors", JSON.stringify(restoredErrors));

        allInputs.forEach(el => {
            el.addEventListener("input", () => {
                const fieldName = el.name;
                let visibleErrors = JSON.parse(sessionStorage.getItem("visibleErrors") || "[]");

                if (el.value.trim() === "") {
                    if (!visibleErrors.includes(fieldName)) visibleErrors.push(fieldName);
                } else {
                    visibleErrors = visibleErrors.filter(f => f !== fieldName);
                }

                if ((fieldName === "email" || fieldName === "phone")) {
                    const contactLi = errorList.querySelector('li[data-field="contact"]');
                    if (contactLi) {
                        if (!el.form.email.value.trim() && !el.form.phone.value.trim()) {
                            if (!visibleErrors.includes("contact")) visibleErrors.push("contact");
                        } else {
                            visibleErrors = visibleErrors.filter(f => f !== "contact");
                        }
                    }
                }

                sessionStorage.setItem("visibleErrors", JSON.stringify(visibleErrors));
                updateErrors();
            });
        });

        updateErrors();
    }
});