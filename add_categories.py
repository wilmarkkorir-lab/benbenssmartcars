import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'benbens_smart_cars.settings')
django.setup()

from cars.models import Category

categories = [
    'Sedan',
    'SUV',
    'Hatchback',
    'Pickup Truck',
    'Minivan / Van',
    'Crossover',
    'Coupe',
    'Luxury',
    'Electric / Hybrid',
    'Sports Car',
    'Convertible',
    'Wagon / Estate',
    'Off-Road / 4x4',
    'Microcar / City Car',
    'Bus / Matatu',
    'Truck / Lorry',
]

created = 0
skipped = 0

for name in categories:
    obj, was_created = Category.objects.get_or_create(name=name)
    if was_created:
        print(f'✅ Created: {name}')
        created += 1
    else:
        print(f'⏭️  Already exists: {name}')
        skipped += 1

print(f'\nDone! {created} created, {skipped} already existed.')
