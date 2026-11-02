(() => {
    const shell = document.querySelector('.page-shell');
    const body = document.getElementById('students-body');
    const search = document.getElementById('student-search');
    const filter = document.getElementById('marks-filter');
    const sort = document.getElementById('student-sort');
    const noResults = document.getElementById('no-results');
    const count = document.getElementById('visible-count');
    const footerCount = document.getElementById('footer-count');

    if (!shell || !body || !search || !filter || !sort) return;

    const total = Number(shell.dataset.total || 0);
    const rows = [...body.querySelectorAll('.student-row')];

    document.querySelectorAll('.mark-fill[data-score]').forEach(bar => {
        const score = Math.max(0, Math.min(100, Number(bar.dataset.score) || 0));
        bar.style.width = `${score}%`;
    });

    function updateRows() {
        const query = search.value.trim().toLowerCase();
        const selected = filter.value;
        const visible = rows.filter(row => {
            const name = row.dataset.name;
            const id = row.dataset.id;
            const marks = Number(row.dataset.marks);
            const matchesQuery = name.includes(query) || id.includes(query);
            const matchesFilter = selected === 'all'
                || (selected === '90' && marks >= 90)
                || (selected === '75' && marks >= 75 && marks < 90)
                || (selected === 'below75' && marks < 75);
            row.hidden = !(matchesQuery && matchesFilter);
            return !row.hidden;
        });

        const mode = sort.value;
        visible.sort((a, b) => {
            if (mode === 'name') return a.dataset.name.localeCompare(b.dataset.name);
            if (mode === 'age') return Number(a.dataset.age) - Number(b.dataset.age);
            if (mode === 'marks-high') return Number(b.dataset.marks) - Number(a.dataset.marks);
            if (mode === 'marks-low') return Number(a.dataset.marks) - Number(b.dataset.marks);
            return Number(a.dataset.id) - Number(b.dataset.id);
        }).forEach(row => body.appendChild(row));

        noResults.hidden = visible.length !== 0 || total === 0;
        count.textContent = visible.length;
        footerCount.textContent = visible.length;
    }

    [search, filter, sort].forEach(control => control.addEventListener('input', updateRows));
    document.addEventListener('keydown', event => {
        if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
            event.preventDefault();
            search.focus();
        }
        if (event.key === 'Escape' && document.activeElement === search) {
            search.value = '';
            updateRows();
            search.blur();
        }
    });
})();
