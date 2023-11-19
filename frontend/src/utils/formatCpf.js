export const formatCPF = (value) => {
    const cleanedValue = value.replace(/\D/g, '');

    const formattedValue = cleanedValue.replace(
        /^(\d{3})(\d{3})(\d{3})(\d{2})$/,
        '$1.$2.$3-$4'
    );

    return formattedValue;
};
