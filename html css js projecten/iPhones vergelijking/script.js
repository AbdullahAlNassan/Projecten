document.addEventListener('DOMContentLoaded', function() {
    const comparisonDiv = document.getElementById('comparison');
    const select1 = document.getElementById('select1');
    const select2 = document.getElementById('select2');
    const scrollButton = document.getElementById('scrollButton'); // Toegevoegd

    const phones = {
        iphone8: {
            model: 'iPhone 8',
            screenSize: '4.7 inch',
            camera: 'Single camera setup',
            price: '$399'
        },
        iphone11: {
            model: 'iPhone 11',
            screenSize: '6.1 inch',
            camera: 'Dual camera setup',
            price: '$699'
        },
        iphone12: {
            model: 'iPhone 12',
            screenSize: '6.1 inch',
            camera: 'Dual camera setup',
            price: '$799'
        },
        iphone13: {
            model: 'iPhone 13',
            screenSize: '6.1 inch',
            camera: 'Dual camera setup',
            price: '$799'
        },
        iphone14: {
            model: 'iPhone 14',
            screenSize: '6.1 inch',
            camera: 'Triple camera setup',
            price: '$899'
        },
        iphone15: {
            model: 'iPhone 15',
            screenSize: '6.7 inch',
            camera: 'Triple camera setup',
            price: '$999'
        }
    };

    function createComparisonCard(phone) {
        const card = document.createElement('div');
        card.classList.add('card', 'mb-3');
        card.innerHTML = `
            <div class="card-body">
                <h2 class="card-title">${phone.model}</h2>
                <p class="card-text"><strong>Screen Size:</strong> ${phone.screenSize}</p>
                <p class="card-text"><strong>Camera:</strong> ${phone.camera}</p>
                <p class="card-text"><strong>Price:</strong> ${phone.price}</p>
            </div>
        `;
        return card;
    }

    function comparePhones() {
        const phone1 = phones[select1.value];
        const phone2 = phones[select2.value];
        
        comparisonDiv.innerHTML = '';
        comparisonDiv.appendChild(createComparisonCard(phone1));
        comparisonDiv.appendChild(createComparisonCard(phone2));
    }

    select1.addEventListener('change', comparePhones);
    select2.addEventListener('change', comparePhones);

    // Scroll-down functionality
    scrollButton.addEventListener('click', function() {
        window.scrollTo({
            top: window.innerHeight,
            behavior: 'smooth'
        });
    });

    // Initial comparison
    comparePhones();
});


