const brandTransform = () => {
    const brandButton = document.querySelector('.brand-button');
    const brandTags = document.querySelectorAll('.brand-marker');

    brandButton.addEventListener('click',()=> {
        //Transform brand tags
        brandTags.forEach((tag, index) => {
            if (tag.style.animation) {
                tag.style.animation = '';
            }
            else {
                tag.style.animation = 'brandTransformAnimation'; 
                tag.style["-webkit-animation-duration"] = `${(4 - index)}s`;
            }
        });
    });
}

// brandTransform();


window.onload = function brandTransform (){
    const brandTags = document.querySelectorAll('.brand-marker');

    brandTags.forEach((tag, index) => {
        if (tag.style.animation) {
            tag.style.animation = '';
        }
        else {
            tag.style.animation = 'brandTransformAnimation'; 
            tag.style["-webkit-animation-duration"] = `${(4 - index)}s`;
        }
    });
}

