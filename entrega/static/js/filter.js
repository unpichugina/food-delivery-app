const filterProduct = document.querySelectorAll('.product');

const sectionName = $('#section').val()

document.querySelector('.new_nav').addEventListener('click', event => {
    if (event.target.tagName !== 'LI') return false;

    let filterClass = event.target.dataset['f'];
    console.log(filterClass);
    filterProduct.forEach( elem  => {
        elem.classList.remove('hide');
        if (!elem.classList.contains(filterClass) && filterClass!== 'all') {
            elem.classList.add('hide');
        }
    });
});
