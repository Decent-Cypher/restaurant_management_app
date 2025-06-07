import React from 'react';

interface FoodItemProps {
  name: string;
  price: string;
  image: string;
}

export default function FoodItem({ name, price, image }: FoodItemProps) {
  return (
    <div className="min-w-[240px] max-w-[240px] overflow-hidden transition-all duration-300">
      <div className="h-[240px] w-full">
        <img 
          src={image} 
          alt={name} 
          className="h-full w-full object-cover"
        />
      </div>
      <div className="flex flex-col justify-between items-start mb-2">
        <div className="text-xl font-medium text-gray-800 line-clamp-2">{name}</div>
        <div className="font-medium text-red-600 whitespace-nowrap">{price}</div>
      </div>
    </div>
  );
}