import sharp from 'sharp';
import { join } from 'path';

const publicDir = join(process.cwd(), 'public');

async function optimizeImages() {
	console.log('Starting image optimization...\n');

	// Optimize logo (256x256 for display, WebP format)
	const logoInput = join(publicDir, 'logo.png');
	const logoOutput = join(publicDir, 'logo.webp');

	await sharp(logoInput)
		.resize(256, 256, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
		.webp({ quality: 85 })
		.toFile(logoOutput);

	const logoStats = await sharp(logoOutput).metadata();
	console.log(`✅ Logo: 256x256 WebP created`);

	// Optimize favicon (64x64 PNG for browser compatibility)
	const faviconOutput = join(publicDir, 'favicon.png');

	await sharp(logoInput)
		.resize(64, 64, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
		.png({ quality: 80 })
		.toFile(faviconOutput + '.tmp');

	// Replace original
	const fs = await import('fs/promises');
	await fs.rename(faviconOutput + '.tmp', faviconOutput);

	console.log(`✅ Favicon: 64x64 PNG created`);

	// Create Apple Touch Icon (180x180)
	const appleIconOutput = join(publicDir, 'apple-touch-icon.png');
	await sharp(logoInput)
		.resize(180, 180, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
		.png({ quality: 85 })
		.toFile(appleIconOutput);

	console.log(`✅ Apple Touch Icon: 180x180 PNG created`);

	// Show size comparison
	const originalSize = (await fs.stat(logoInput)).size;
	const newLogoSize = (await fs.stat(logoOutput)).size;
	const newFaviconSize = (await fs.stat(faviconOutput)).size;
	const newAppleSize = (await fs.stat(appleIconOutput)).size;

	console.log('\n📊 Size comparison:');
	console.log(`   Original: ${(originalSize / 1024).toFixed(1)} KB`);
	console.log(`   Logo WebP: ${(newLogoSize / 1024).toFixed(1)} KB`);
	console.log(`   Favicon: ${(newFaviconSize / 1024).toFixed(1)} KB`);
	console.log(`   Apple Icon: ${(newAppleSize / 1024).toFixed(1)} KB`);
	console.log(`   Total new: ${((newLogoSize + newFaviconSize + newAppleSize) / 1024).toFixed(1)} KB`);
	console.log(`   Reduction: ${(100 - (newLogoSize + newFaviconSize + newAppleSize) / (originalSize * 2) * 100).toFixed(1)}%`);

	// Remove original large PNG
	await fs.unlink(logoInput);
	console.log('\n🗑️  Removed original large logo.png');

	console.log('\n✨ Optimization complete!');
}

optimizeImages().catch((error) => {
	console.error('Image optimization failed:', error);
	process.exit(1);
});
