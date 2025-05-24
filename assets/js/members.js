// Initialize Select2 for better dropdown experience
$(document).ready(function() {
    $('.filter-select').select2({
        width: '100%'
    });

    // Load member data from Excel file
    loadMemberData();
});

let membersData = [];

async function loadMemberData() {
    try {
        // Replace this with actual Excel file path
        const response = await fetch('assets/data/members.json');
        membersData = await response.json();
        
        // Populate filter dropdowns
        populateFilters();
        
        // Display all members initially
        displayMembers(membersData);
    } catch (error) {
        console.error('Error loading member data:', error);
    }
}

function populateFilters() {
    // Get unique values for each filter
    const designations = [...new Set(membersData.map(m => m.designation))].sort();
    const provinces = [...new Set(membersData.map(m => m.province))].sort();
    const cities = [...new Set(membersData.map(m => m.city))].sort();

    // Populate designation filter
    designations.forEach(designation => {
        $('#designationFilter').append(
            $('<option>', {
                value: designation,
                text: designation
            })
        );
    });

    // Populate province filter
    provinces.forEach(province => {
        $('#provinceFilter').append(
            $('<option>', {
                value: province,
                text: province
            })
        );
    });

    // Populate city filter
    cities.forEach(city => {
        $('#cityFilter').append(
            $('<option>', {
                value: city,
                text: city
            })
        );
    });

    // Add filter change event handlers
    $('.filter-select').on('change', function() {
        applyFilters();
    });
}

function applyFilters() {
    const gender = $('#genderFilter').val();
    const designation = $('#designationFilter').val();
    const province = $('#provinceFilter').val();
    const city = $('#cityFilter').val();

    const filteredMembers = membersData.filter(member => {
        return (!gender || member.gender === gender) &&
               (!designation || member.designation === designation) &&
               (!province || member.province === province) &&
               (!city || member.city === city);
    });

    displayMembers(filteredMembers);
}

function displayMembers(members) {
    const grid = $('#membersGrid');
    grid.empty();

    members.forEach(member => {
        const memberCard = `
            <div class="col-lg-3 col-md-4 col-sm-6">
                <div class="card h-100" style="cursor: pointer;" onclick="showMemberDetails(${member.id})">
                    <img src="${member.photo_url || 'assets/images/default-avatar.svg'}" 
                         class="card-img-top" alt="${member.name}"
                         style="height: 200px; object-fit: cover;">
                    <div class="card-body">
                        <h5 class="card-title">${member.name}</h5>
                        <p class="card-text text-muted mb-0">${member.designation}</p>
                        <p class="card-text"><small class="text-muted">${member.city}, ${member.province}</small></p>
                    </div>
                </div>
            </div>
        `;
        grid.append(memberCard);
    });
}

function showMemberDetails(memberId) {
    const member = membersData.find(m => m.id === memberId);
    if (!member) return;

    $('#memberPhoto').attr('src', member.photo_url || 'assets/images/default-avatar.svg');
    $('#memberName').text(member.name);
    $('#memberDesignation').text(member.designation);

    const details = `
        <div class="row">
            <div class="col-md-6">
                <p><strong>Gender:</strong> ${member.gender}</p>
                <p><strong>City:</strong> ${member.city}</p>
                <p><strong>Province:</strong> ${member.province}</p>
            </div>
            <div class="col-md-6">
                <p><strong>Institution:</strong> ${member.institution || 'N/A'}</p>
                <p><strong>Specialization:</strong> ${member.specialization || 'N/A'}</p>
                <p><strong>Email:</strong> ${member.email || 'N/A'}</p>
            </div>
        </div>
        ${member.bio ? `<div class="mt-3"><strong>Bio:</strong><p>${member.bio}</p></div>` : ''}
        ${member.research_interests ? `<div class="mt-3"><strong>Research Interests:</strong><p>${member.research_interests}</p></div>` : ''}
    `;

    $('#memberDetails').html(details);
    new bootstrap.Modal($('#memberModal')).show();
} 