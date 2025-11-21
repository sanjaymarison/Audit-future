function closeit() {
	// Add smooth fade out animation before closing
	document.body.style.opacity = '0';
	document.body.style.transition = 'opacity 0.5s ease';
	setTimeout(function() {
		window.close();
	}, 500);
}

// Add smooth scroll behavior
document.addEventListener('DOMContentLoaded', function() {
	// Smooth scroll for anchor links
	document.querySelectorAll('a[href^="#"]').forEach(anchor => {
		anchor.addEventListener('click', function (e) {
			e.preventDefault();
			const target = document.querySelector(this.getAttribute('href'));
			if (target) {
				target.scrollIntoView({
					behavior: 'smooth',
					block: 'start'
				});
			}
		});
	});
	
	// Add animation to list items on scroll
	const observerOptions = {
		threshold: 0.1,
		rootMargin: '0px 0px -50px 0px'
	};
	
	const observer = new IntersectionObserver(function(entries) {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				entry.target.style.opacity = '1';
				entry.target.style.transform = 'translateY(0)';
			}
		});
	}, observerOptions);
	
	// Observe all list items
	document.querySelectorAll('li').forEach(item => {
		item.style.opacity = '0';
		item.style.transform = 'translateY(20px)';
		item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
		observer.observe(item);
	});
	
	// Add ripple effect to buttons
	document.querySelectorAll('.button').forEach(button => {
		button.addEventListener('click', function(e) {
			const ripple = document.createElement('span');
			const rect = button.getBoundingClientRect();
			const size = Math.max(rect.width, rect.height);
			const x = e.clientX - rect.left - size / 2;
			const y = e.clientY - rect.top - size / 2;
			
			ripple.style.width = ripple.style.height = size + 'px';
			ripple.style.left = x + 'px';
			ripple.style.top = y + 'px';
			ripple.classList.add('ripple');
			
			const rippleEffect = button.querySelector('.ripple');
			if (rippleEffect) {
				rippleEffect.remove();
			}
			
			button.appendChild(ripple);
		});
	});
});
