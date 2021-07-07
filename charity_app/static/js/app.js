document.addEventListener("DOMContentLoaded", function () {
    /**
     * HomePage - Help section
     */
    class Help {
        constructor($el) {
            this.$el = $el;
            this.$buttonsContainer = $el.querySelector(".help--buttons");
            this.$slidesContainers = $el.querySelectorAll(".help--slides");
            this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
            this.init();
        }

        init() {
            this.events();
        }

        events() {
            /**
             * Slide buttons
             */
            this.$buttonsContainer.addEventListener("click", e => {
                if (e.target.classList.contains("btn")) {
                    this.changeSlide(e);
                }
            });

            /**
             * Pagination buttons
             */
            this.$el.addEventListener("click", e => {
                if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
                    this.changePage(e);
                }
            });
        }

        changeSlide(e) {
            e.preventDefault();
            const $btn = e.target;

            // Buttons Active class change
            [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
            $btn.classList.add("active");

            // Current slide
            this.currentSlide = $btn.parentElement.dataset.id;

            // Slides active class change
            this.$slidesContainers.forEach(el => {
                el.classList.remove("active");

                if (el.dataset.id === this.currentSlide) {
                    el.classList.add("active");
                }
            });
        }

        /**
         * TODO: callback to page change event
         */
        changePage(e) {
            e.preventDefault();
            const page = e.target.dataset.page;

            console.log(page);
        }
    }

    const helpSection = document.querySelector(".help");
    if (helpSection !== null) {
        new Help(helpSection);
    }

    /**
     * Form Select
     */
    class FormSelect {
        constructor($el) {
            this.$el = $el;
            this.options = [...$el.children];
            this.init();
        }

        init() {
            this.createElements();
            this.addEvents();
            this.$el.parentElement.removeChild(this.$el);
        }

        createElements() {
            // Input for value
            this.valueInput = document.createElement("input");
            this.valueInput.type = "text";
            this.valueInput.name = this.$el.name;

            // Dropdown container
            this.dropdown = document.createElement("div");
            this.dropdown.classList.add("dropdown");

            // List container
            this.ul = document.createElement("ul");

            // All list options
            this.options.forEach((el, i) => {
                const li = document.createElement("li");
                li.dataset.value = el.value;
                li.innerText = el.innerText;

                if (i === 0) {
                    // First clickable option
                    this.current = document.createElement("div");
                    this.current.innerText = el.innerText;
                    this.dropdown.appendChild(this.current);
                    this.valueInput.value = el.value;
                    li.classList.add("selected");
                }

                this.ul.appendChild(li);
            });

            this.dropdown.appendChild(this.ul);
            this.dropdown.appendChild(this.valueInput);
            this.$el.parentElement.appendChild(this.dropdown);
        }

        addEvents() {
            this.dropdown.addEventListener("click", e => {
                const target = e.target;
                this.dropdown.classList.toggle("selecting");

                // Save new value only when clicked on li
                if (target.tagName === "LI") {
                    this.valueInput.value = target.dataset.value;
                    this.current.innerText = target.innerText;
                }
            });
        }
    }

    document.querySelectorAll(".form-group--dropdown select").forEach(el => {
        new FormSelect(el);
    });

    /**
     * Hide elements when clicked on document
     */
    document.addEventListener("click", function (e) {
        const target = e.target;
        const tagName = target.tagName;

        if (target.classList.contains("dropdown")) return false;

        if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
            return false;
        }

        if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
            return false;
        }

        document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
            el.classList.remove("selecting");
        });
    });

    /**
     * Switching between form steps
     */
    class FormSteps {
        constructor(form) {
            this.$form = form;
            this.$next = form.querySelectorAll(".next-step");
            this.$prev = form.querySelectorAll(".prev-step");
            this.$step = form.querySelector(".form--steps-counter span");
            this.currentStep = 1;

            this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
            const $stepForms = form.querySelectorAll("form > div");
            this.slides = [...this.$stepInstructions, ...$stepForms];


            this.init();
        }

        /**
         * Init all methods
         */
        init() {
            this.events();
            this.updateForm();
        }

        /**
         * All events that are happening in form
         */
        events() {
            // Next step
            this.$next.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep++;
                    this.updateForm();
                });
            });

            // Previous step
            this.$prev.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep--;
                    this.updateForm();
                });
            });

            // Form submit
            this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
        }

        /**
         * Update form front-end
         * Show next or previous section etc.
         */
        updateForm() {
            this.$step.innerText = this.currentStep;


            // TODO: Validation

            if (this.currentStep === 2){
                const categories = document.querySelectorAll('input[type=checkbox]')
                let checked = 0
                for (let category of categories){
                if (category.checked){
                    checked += 1
                }}

                if (checked === 0){
                    this.currentStep = 1
                    const error = document.querySelector('.error-categories')
                    error.innerText = 'Zaznacz kategorię rzeczy, które chcesz oddać'
                }
            }


            if (this.currentStep === 3){
                if (document.forms["charityForm"]["bags-amount"].value === ''){
                    this.currentStep = 2
                    const error = document.querySelector('.error-bags')
                    error.innerText = 'Podaj liczbę worków'
                }
            }

            if (this.currentStep === 4){
                const organization = document.querySelectorAll('input[type=radio]')
                let checked = 0

                for (let org of organization){
                if (org.checked){
                    checked += 1
                }}

                if (checked === 0){
                    this.currentStep = 3;
                    const error = document.querySelector('.error-organization')
                    error.innerText = 'Zaznacz organizację, której chcesz pomóc'
                }
            }

            if (this.currentStep === 5){
                if (document.forms["charityForm"]["address"].value === ''||
                    document.forms["charityForm"]["city"].value === '' ||
                    document.forms["charityForm"]["postcode"].value === '' ||
                    document.forms["charityForm"]["date"].value === '' ||
                    document.forms["charityForm"]["time"].value === ''){
                    this.currentStep = 4
                    const error = document.querySelector('.error-address')
                    error.innerText = 'Pola z gwiazdką są obowiązkowe'
                }
            }

            this.slides.forEach(slide => {
                slide.classList.remove("active");

                if (slide.dataset.step == this.currentStep) {
                    slide.classList.add("active");
                }
            });

            this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
            this.$step.parentElement.hidden = this.currentStep >= 6;

            // TODO: get data from inputs and show them in summary

            const categories = document.querySelectorAll('input[name="categories"]:checked')
            const catInfo = document.querySelector('.categories')

            const bags = document.getElementsByName('bags-amount')[0]
            const bagsInfo = document.querySelector('.bags')
            const bagsDecl = document.querySelector('.bagsDecl')

            const organization = document.querySelector('input[name="organization-name"]:checked')
            const orgInfo = document.querySelector('.organization')

            const address = document.getElementsByName('address')[0]
            const city = document.getElementsByName('city')[0]
            const postcode = document.getElementsByName('postcode')[0]
            const phone = document.getElementsByName('phone')[0]
            const date = document.getElementsByName('date')[0]
            const time = document.getElementsByName('time')[0]
            const moreInfo = document.getElementsByName('more_info')[0]
            const addressInfos = document.querySelectorAll('.address-info li')
            const dateInfos = document.querySelectorAll('.date-info li')

            if (this.currentStep === 5){
                bagsInfo.innerText = bags.value
                let bagsValue = parseInt(bags.value)
                if (bagsValue === 1){
                    bagsDecl.innerText = "worek"
                }
                else if (bagsValue > 1 && bagsValue < 5){
                    bagsDecl.innerText = "worki"
                }
                else {
                    bagsDecl.innerText = "worków"
                }

                let catValue = []
                function getCategories(array){
                for (let cat of array){
                    catValue.push(cat.value)
                }
                return catValue}
                catInfo.innerText = getCategories(categories)
                debugger

                orgInfo.innerText = organization.value
                addressInfos[0].innerText = address.value
                addressInfos[1].innerText = city.value
                addressInfos[2].innerText = postcode.value
                addressInfos[3].innerText = phone.value
                dateInfos[0].innerText = date.value
                dateInfos[1].innerText = time.value
                dateInfos[2].innerText = moreInfo.value
            }
        }

        /**
         * Submit form
         *
         * TODO: validation, send data to server
         */


        submit(e) {
          e.preventDefault();
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');

          $.ajax({
              type: 'POST',
              url: '/add_donation/',
              headers: {'X-CSRFToken': csrftoken},
              data: {
                  quantity: $('input[name="bags-amount"]').val(),
                  categories: $('input[name="categories"]').val(),
                  institution: $('input[name="organization-name"]').val(),
                  address: $('input[name="address"]').val(),
                  city: $('input[name="city"]').val(),
                  phone_number: $('input[name="phone"]').val(),
                  zip_code: $('input[name="postcode"]').val(),
                  pick_up_date: $('input[name="date"]').val(),
                  pick_up_time: $('input[name="time"]').val(),
                  pick_up_comment: $('input[name="more_info"]').val(),
                  csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
              }
          });
            this.currentStep++;
          this.updateForm();
        }
    }

    const form = document.querySelector(".form--steps");
    if (form !== null) {
        new FormSteps(form);
    }
});
