if (this.currentStep === 2){
                const categories = document.querySelectorAll('input[type=checkbox]')
                let checked = 0
                for (let category of categories){
                if (category.checked){
                    checked += 1
                }
                if (checked === 0){
                    this.currentStep = 1
                    const error = document.querySelector('.error-categories')
                    error.innerText = 'Zaznacz kategorię rzeczy, które chcesz oddać'
                }
                else {
                    this.currentStep = 2
                }
                }
            }

            if (this.currentStep === 3){
                if (document.forms["charityForm"]["bags"].value === ''){
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
                }
                if (checked === 0){
                    this.currentStep = 3;
                    const error = document.querySelector('.error-organization')
                    error.innerText = 'Zaznacz organizację, której chcesz pomóc'
                }
                else {
                    this.currentStep = 4
                }}
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
                else {
                    this.currentStep = 5
                }
            }
